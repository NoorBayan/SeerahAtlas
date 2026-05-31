import json
import zipfile
import os

class AtlasDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.records = self._load_data()
        self.dimensions_list = []
        self.tags_by_dimension = {}
        self.sdg_list = []
        self.maqasid_list = []
        self.keywords_list = []
        self._extract_filters()

    def _load_data(self):
        try:
            # التحقق مما إذا كان الملف الممرر هو ملف مضغوط ZIP
            if self.filepath.endswith('.zip'):
                # فتح ملف الـ ZIP في الذاكرة (دون الحاجة لاستخراج الملف فعلياً على الهارد)
                with zipfile.ZipFile(self.filepath, 'r') as z:
                    # نفترض أن ملف الـ JSON داخل الـ ZIP يحمل نفس اسم الملف ولكن بصيغة json
                    json_filename = os.path.basename(self.filepath).replace('.zip', '.json')
                    
                    # قراءة محتوى الـ JSON من داخل الـ ZIP
                    with z.open(json_filename) as f:
                        data = json.load(f)
            else:
                # إذا كان ملف JSON عادي (في حال قررت استخدامه محلياً)
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
            if isinstance(data, dict):
                return list(data.values())[0] if data.values() else []
            return data
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def _extract_filters(self):
        dimensions_set = set()
        sdgs_set = set()
        maqasid_set = set()
        keywords_set = set() # <-- مصفوفة جديدة لجمع الكلمات المفتاحية
        
        for record in self.records:
            for unit in record.get('semantic_units', []):
                dims = unit['semantic_core'].get('sustainability_dimensions', [])
                tags = unit['semantic_core'].get('domain_tags', [])
                
                sdgs = unit.get('unit_interpretive_layer', {}).get('global_sdg_mapping', {}).get('sdg_goal', [])
                for sdg in sdgs:
                    sdgs_set.add(sdg)
                    
                maqasid = unit['semantic_core'].get('maqasid_alignment', [])
                for maq in maqasid:
                    maqasid_set.add(maq)
                
                # استخراج الكلمات المفتاحية (Keywords)
                keywords = unit['semantic_core'].get('keywords', [])
                for kw in keywords:
                    keywords_set.add(kw)
                
                for dim in dims:
                    dimensions_set.add(dim)
                    if dim not in self.tags_by_dimension:
                        self.tags_by_dimension[dim] = set()
                    for tag in tags:
                        if tag.startswith(dim):
                            self.tags_by_dimension[dim].add(tag)
                            
        self.dimensions_list = sorted(list(dimensions_set))
        self.sdg_list = sorted(list(sdgs_set))
        self.maqasid_list = sorted(list(maqasid_set))
        self.keywords_list = sorted(list(keywords_set)) # <-- ترتيب قائمة الكلمات المفتاحية
        
        for dim in self.tags_by_dimension:
            self.tags_by_dimension[dim] = sorted(list(self.tags_by_dimension[dim]))
