import json

class AtlasDataLoader:
    def __init__(self, filepath):
        self.maqasid_list = []
        self.filepath = filepath
        self.records = self._load_data()
        self.dimensions_list = []
        self.tags_by_dimension = {}
        self.sdg_list = [] # قائمة جديدة لأهداف التنمية
        self._extract_filters()

    def _load_data(self):
        try:
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
        maqasid_set = set() # <-- مصفوفة جديدة لجمع المقاصد الشرعية
        
        for record in self.records:
            for unit in record.get('semantic_units', []):
                dims = unit['semantic_core'].get('sustainability_dimensions', [])
                tags = unit['semantic_core'].get('domain_tags', [])
                
                # استخراج الـ SDGs
                sdgs = unit.get('unit_interpretive_layer', {}).get('global_sdg_mapping', {}).get('sdg_goal', [])
                for sdg in sdgs:
                    sdgs_set.add(sdg)
                    
                # استخراج المقاصد الشرعية (Maqasid)
                maqasid = unit['semantic_core'].get('maqasid_alignment', [])
                for maq in maqasid:
                    maqasid_set.add(maq)
                
                for dim in dims:
                    dimensions_set.add(dim)
                    if dim not in self.tags_by_dimension:
                        self.tags_by_dimension[dim] = set()
                    for tag in tags:
                        if tag.startswith(dim):
                            self.tags_by_dimension[dim].add(tag)
                            
        self.dimensions_list = sorted(list(dimensions_set))
        self.sdg_list = sorted(list(sdgs_set))
        self.maqasid_list = sorted(list(maqasid_set)) # <-- ترتيب قائمة المقاصد
        
        for dim in self.tags_by_dimension:
            self.tags_by_dimension[dim] = sorted(list(self.tags_by_dimension[dim]))
