import json

class AtlasDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.records = self._load_data()
        self.dimensions_list = []
        self.tags_by_dimension = {}
        self._extract_filters()

    def _load_data(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # التأكد من أن البيانات عبارة عن قائمة من السجلات
                if isinstance(data, dict):
                    # إذا كان الجايسون يبدأ بـ Object داخله قائمة
                    return list(data.values())[0] if data.values() else []
                return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def _extract_filters(self):
        dimensions_set = set()
        for record in self.records:
            for unit in record.get('semantic_units', []):
                dims = unit['semantic_core'].get('sustainability_dimensions', [])
                tags = unit['semantic_core'].get('domain_tags', [])
                
                for dim in dims:
                    dimensions_set.add(dim)
                    if dim not in self.tags_by_dimension:
                        self.tags_by_dimension[dim] = set()
                    for tag in tags:
                        if tag.startswith(dim):
                            self.tags_by_dimension[dim].add(tag)
                            
        self.dimensions_list = sorted(list(dimensions_set))
        # تحويل الـ Sets إلى Lists مرتبة
        for dim in self.tags_by_dimension:
            self.tags_by_dimension[dim] = sorted(list(self.tags_by_dimension[dim]))
