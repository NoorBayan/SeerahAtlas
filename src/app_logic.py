import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from src.data_loader import AtlasDataLoader
from src.templates import template_architectural_explorer

class AtlasApp:
    def __init__(self, data_path):
        self.data_loader = AtlasDataLoader(data_path)
        self.records = self.data_loader.records
        self._setup_widgets()

    def _setup_widgets(self):
        # القوائم المنسدلة
        self.drop_template = widgets.Dropdown(
            options={'المشرح المعماري (Architectural Explorer)': template_architectural_explorer},
            description='القالب:', style={'description_width': 'initial'})
        
        self.drop_dim = widgets.Dropdown(
            options=self.data_loader.dimensions_list, 
            description='البعد المستدام:', style={'description_width': 'initial'})
            
        self.drop_tag = widgets.Dropdown(
            options=[], description='الوسم الدلالي:', style={'description_width': 'initial'})
            
        self.drop_hadith = widgets.Dropdown(
            options=[], description='الحديث:', style={'description_width': 'initial'}, layout=widgets.Layout(width='300px'))
            
        self.output_area = widgets.Output()

        # ربط الأحداث (Events)
        self.drop_dim.observe(self.update_tags, 'value')
        self.drop_tag.observe(self.update_hadiths, 'value')
        self.drop_hadith.observe(self.render_view, 'value')
        self.drop_template.observe(self.render_view, 'value')

        # التهيئة الأولية
        if self.data_loader.dimensions_list:
            self.drop_dim.value = self.data_loader.dimensions_list[0]
            self.update_tags(None)

    def update_tags(self, change):
        dim = self.drop_dim.value
        tags = self.data_loader.tags_by_dimension.get(dim, [])
        self.drop_tag.options = tags
        if tags:
            self.drop_tag.value = tags[0]
            self.update_hadiths(None)

    def update_hadiths(self, change):
        tag = self.drop_tag.value
        matched = []
        for r in self.records:
            for u in r.get('semantic_units', []):
                if tag in u.get('semantic_core', {}).get('domain_tags', []):
                    hid = r.get('hadith_core', {}).get('hadith_id', 'Unknown')
                    # عرض رقم الحديث كخيار، وقيمة الخيار هي السجل نفسه
                    matched.append((f"حديث رقم: {hid}", r))
                    break
        self.drop_hadith.options = matched
        if matched:
            self.drop_hadith.value = matched[0][1]
            self.render_view(None)

    def render_view(self, change):
        with self.output_area:
            clear_output(wait=True)
            record = self.drop_hadith.value
            template_func = self.drop_template.value
            if record and template_func:
                html_content = template_func(record)
                display(HTML(html_content))

    def run(self):
        # التعديل هنا: استخدام widgets.HTML بدلاً من HTML
        header = widgets.HTML(value="<h2 style='text-align:right; color:#2c3e50; font-family:Tahoma, sans-serif;'>أطلس الاستدامة النبوي: لوحة التحكم التفاعلية</h2><hr>")
        
        controls_row1 = widgets.HBox([self.drop_dim, self.drop_tag])
        controls_row2 = widgets.HBox([self.drop_hadith, self.drop_template])
        
        ui = widgets.VBox([header, controls_row1, controls_row2, self.output_area])
        display(ui)


from src.templates import template_sdg_policy_map

class SDGPolicyApp:
    def __init__(self, data_path):
        self.data_loader = AtlasDataLoader(data_path)
        self.records = self.data_loader.records
        self._setup_widgets()

    def _setup_widgets(self):
        # القائمة المنسدلة الوحيدة هنا هي الخاصة بأهداف الأمم المتحدة
        self.drop_sdg = widgets.Dropdown(
            options=self.data_loader.sdg_list,
            description='الهدف التنموي (SDG):', 
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='400px')
        )
        self.output_area = widgets.Output()

        # المراقبة
        self.drop_sdg.observe(self.render_view, 'value')

    def render_view(self, change=None):
        with self.output_area:
            clear_output(wait=True)
            selected_sdg = self.drop_sdg.value
            
            # البحث عن كل الوحدات (ASUs) التي تحتوي على هذا الهدف
            matched_units = []
            for r in self.records:
                hid = r.get('hadith_core', {}).get('hadith_id', 'Unknown')
                for u in r.get('semantic_units', []):
                    sdgs = u.get('unit_interpretive_layer', {}).get('global_sdg_mapping', {}).get('sdg_goal', [])
                    if selected_sdg in sdgs:
                        matched_units.append({'hadith_id': hid, 'unit': u})
            
            # إرسال البيانات للقالب الجديد
            if selected_sdg:
                html_content = template_sdg_policy_map(matched_units, selected_sdg)
                display(HTML(html_content))

    def run(self):
        header = widgets.HTML(value="<h2 style='text-align:right; color:#d35400; font-family:Tahoma, sans-serif;'>خارطة السياسات المعاصرة (SDG & Policy Map)</h2><p style='text-align:right;'>اختر هدف التنمية المستدامة لاستعراض السياسات الحديثة المدعومة بالتوجيهات النبوية.</p><hr>")
        ui = widgets.VBox([header, self.drop_sdg, self.output_area])
        display(ui)
        self.render_view() # عرض النتيجة الأولى مباشرة

from src.templates import template_maqasid_observatory

class MaqasidApp:
    def __init__(self, data_path):
        self.data_loader = AtlasDataLoader(data_path)
        self.records = self.data_loader.records
        self._setup_widgets()

    def _setup_widgets(self):
        self.drop_maqsad = widgets.Dropdown(
            options=self.data_loader.maqasid_list,
            description='المقصد الشرعي:', 
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='400px')
        )
        self.output_area = widgets.Output()

        self.drop_maqsad.observe(self.render_view, 'value')

    def render_view(self, change=None):
        with self.output_area:
            clear_output(wait=True)
            selected_maqsad = self.drop_maqsad.value
            
            matched_units = []
            for r in self.records:
                hid = r.get('hadith_core', {}).get('hadith_id', 'Unknown')
                for u in r.get('semantic_units', []):
                    maqasid = u.get('semantic_core', {}).get('maqasid_alignment', [])
                    if selected_maqsad in maqasid:
                        matched_units.append({'hadith_id': hid, 'unit': u})
            
            if selected_maqsad:
                html_content = template_maqasid_observatory(matched_units, selected_maqsad)
                display(HTML(html_content))

    def run(self):
        header = widgets.HTML(value="<h2 style='text-align:right; color:#344955; font-family:Tahoma, sans-serif;'>المرصد المقاصدي للاستدامة (Maqasid Observatory)</h2><p style='text-align:right;'>اختر المقصد الشرعي (الضروريات الخمس وما يلحق بها) لاستعراض القواعد والمبادئ النبوية المندرجة تحته.</p><hr>")
        ui = widgets.VBox([header, self.drop_maqsad, self.output_area])
        display(ui)
        self.render_view()


from src.templates import template_thematic_aggregator

class ThematicAggregatorApp:
    def __init__(self, data_path):
        self.data_loader = AtlasDataLoader(data_path)
        self.records = self.data_loader.records
        self._setup_widgets()

    def _setup_widgets(self):
        self.drop_keyword = widgets.Dropdown(
            options=self.data_loader.keywords_list,
            description='الكلمة المفتاحية:', 
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='400px')
        )
        self.output_area = widgets.Output()
        self.drop_keyword.observe(self.render_view, 'value')

    def render_view(self, change=None):
        with self.output_area:
            clear_output(wait=True)
            selected_keyword = self.drop_keyword.value
            
            matched_units = []
            for r in self.records:
                hid = r.get('hadith_core', {}).get('hadith_id', 'Unknown')
                for u in r.get('semantic_units', []):
                    keywords = u.get('semantic_core', {}).get('keywords', [])
                    if selected_keyword in keywords:
                        matched_units.append({'hadith_id': hid, 'unit': u})
            
            if selected_keyword:
                html_content = template_thematic_aggregator(matched_units, selected_keyword)
                display(HTML(html_content))

    def run(self):
        header = widgets.HTML(value="<h2 style='text-align:right; color:#16a085; font-family:Tahoma, sans-serif;'>المجمع الموضوعي للتوجيهات (Thematic Aggregator)</h2><p style='text-align:right;'>اختر كلمة مفتاحية لاستعراض كافة التوجيهات النبوية المرتبطة بها في سياق سردي متصل لبناء فقه موضوعي.</p><hr>")
        ui = widgets.VBox([header, self.drop_keyword, self.output_area])
        display(ui)
        self.render_view()


import plotly.graph_objects as go
from collections import Counter
# (تأكد من أن هذه الاستدعاءات موجودة في أعلى الملف)

class StatisticalDashboardApp:
    def __init__(self, data_path):
        self.data_loader = AtlasDataLoader(data_path)
        self.records = self.data_loader.records
        self.output_area = widgets.Output()

    def generate_kpis(self):
        """حساب مؤشرات الأداء الرئيسية"""
        total_hadiths = len(self.records)
        total_asus = sum(len(r.get('semantic_units', [])) for r in self.records)
        
        # تصميم كروت المؤشرات (KPI Cards)
        html = f"""
        <div style="display: flex; justify-content: space-around; margin-bottom: 30px; direction: rtl;">
            <div style="background: linear-gradient(135deg, #1abc9c, #16a085); color: white; padding: 20px; border-radius: 10px; width: 45%; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <div style="font-size: 16px; font-family: 'Tajawal', sans-serif;">إجمالي الأحاديث النبوية (Records)</div>
                <div style="font-size: 40px; font-weight: bold; margin-top: 10px;">{total_hadiths}</div>
            </div>
            <div style="background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 20px; border-radius: 10px; width: 45%; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <div style="font-size: 16px; font-family: 'Tajawal', sans-serif;">إجمالي الوحدات الذرية المستخلصة (ASUs)</div>
                <div style="font-size: 40px; font-weight: bold; margin-top: 10px;">{total_asus}</div>
            </div>
        </div>
        """
        return widgets.HTML(value=html)

    def generate_pie_chart(self):
        """توليد المخطط الدائري لأبعاد الاستدامة"""
        dims_counter = Counter()
        for r in self.records:
            for u in r.get('semantic_units', []):
                dims = u.get('semantic_core', {}).get('sustainability_dimensions', [])
                for d in dims:
                    dims_counter[d] += 1
                    
        labels = list(dims_counter.keys())
        values = list(dims_counter.values())
        
        # ترجمة الأبعاد لتكون أوضح
        dim_names = {"ECO": "الاقتصاد", "SOC": "المجتمع", "ETH": "الأخلاق", "GOV": "الحوكمة/السياسة"}
        display_labels = [dim_names.get(l, l) for l in labels]

        fig = go.Figure(data=[go.Pie(labels=display_labels, values=values, hole=.4)])
        fig.update_layout(
            title_text="توزيع التوجيهات النبوية على أبعاد الاستدامة (Dimensions)",
            title_x=0.5,
            font=dict(family="Tahoma", size=14)
        )
        return fig

    def generate_bar_chart(self):
        """توليد المخطط الشريطي لأهداف التنمية (SDGs)"""
        sdgs_counter = Counter()
        for r in self.records:
            for u in r.get('semantic_units', []):
                sdgs = u.get('unit_interpretive_layer', {}).get('global_sdg_mapping', {}).get('sdg_goal', [])
                for s in sdgs:
                    sdgs_counter[s] += 1
                    
        # ترتيب الأهداف تنازلياً حسب التغطية
        sorted_sdgs = sdgs_counter.most_common(10) # نأخذ أعلى 10 أهداف لتوضيح الرسم
        
        if not sorted_sdgs:
            return None # إذا كانت البيانات فارغة

        labels = [item[0].replace("SDG_", "").replace("_", " ") for item in sorted_sdgs]
        values = [item[1] for item in sorted_sdgs]

        fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color='#e67e22')])
        fig.update_layout(
            title_text="أكثر أهداف التنمية المستدامة (SDGs) تغطيةً في السنة النبوية",
            title_x=0.5,
            xaxis_title="هدف التنمية المستدامة",
            yaxis_title="عدد التوجيهات النبوية (ASUs)",
            font=dict(family="Tahoma", size=14)
        )
        return fig

    def render_view(self, change=None):
        with self.output_area:
            clear_output(wait=True)
            
            # عرض مؤشرات الأداء (KPIs)
            display(self.generate_kpis())
            
            # عرض المخطط الدائري
            pie_fig = self.generate_pie_chart()
            if pie_fig:
                pie_fig.show()
                
            # عرض المخطط الشريطي
            bar_fig = self.generate_bar_chart()
            if bar_fig:
                bar_fig.show()

    def run(self):
        header = widgets.HTML(value="<h2 style='text-align:right; color:#8e44ad; font-family:Tahoma, sans-serif;'>لوحة القيادة الإحصائية (Statistical Dashboard)</h2><p style='text-align:right;'>نظرة بانورامية تحلّل توزيع التوجيهات النبوية على أبعاد الاستدامة وأهداف الأمم المتحدة.</p><hr>")
        
        btn_refresh = widgets.Button(description="تحديث الإحصائيات", button_style='primary', icon='refresh')
        btn_refresh.on_click(self.render_view)
        
        ui = widgets.VBox([header, btn_refresh, self.output_area])
        display(ui)
        self.render_view()
