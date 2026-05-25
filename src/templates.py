def template_architectural_explorer(record):
    """قالب العرض الأول: المشرح المعماري للوحدات الذرية"""
    
    hadith_id = record.get('hadith_core', {}).get('hadith_id', 'Unknown')
    hadith_text = record.get('hadith_core', {}).get('hadith_text', '')
    context = record.get('global_context', {}).get('discourse_context', '')
    
    html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
        .atlas-container {{ font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; background: #f8f9fa; padding: 20px; border-radius: 10px; max-width: 1000px; margin: auto; }}
        .header-box {{ background: #2c3e50; color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; justify-content: space-between; }}
        .macro-text {{ font-size: 18px; line-height: 1.8; color: #34495e; padding: 15px; background: white; border-right: 5px solid #bdc3c7; border-radius: 5px; margin-bottom: 20px; }}
        .asu-card {{ background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 4px solid #27ae60; }}
        .tag-badge {{ background: #e8f5e9; color: #2e7d32; padding: 5px 12px; border-radius: 20px; font-size: 13px; margin-left: 5px; font-weight: bold; display: inline-block; margin-bottom:5px;}}
        .sdg-badge {{ background: #e3f2fd; color: #1565c0; padding: 5px 12px; border-radius: 20px; font-size: 13px; margin-left: 5px; font-weight: bold; display: inline-block; margin-bottom:5px;}}
        .section-title {{ color: #2980b9; font-size: 15px; font-weight: bold; margin-top: 15px; margin-bottom: 8px; border-bottom: 1px solid #eee; padding-bottom: 3px;}}
        .asu-text {{ font-size: 17px; font-weight: bold; color: #2c3e50; line-height: 1.6; background: #ecf0f1; padding: 10px; border-radius: 5px;}}
        .asu-expl {{ font-size: 15px; color: #555; line-height: 1.6; }}
    </style>

    <div class="atlas-container">
        <div class="header-box">
            <span><strong>رقم السجل:</strong> {hadith_id}</span>
            <span><strong>السياق العام:</strong> {context}</span>
        </div>
        
        <div style="font-weight:bold; color:#7f8c8d; margin-bottom:5px;">النص الأصلي (Document Level):</div>
        <div class="macro-text">{hadith_text}</div>
        
        <div style="font-weight:bold; color:#27ae60; margin-bottom:10px; font-size: 18px;">الوحدات الدلالية المعزولة (ASUs):</div>
    """
    
    for unit in record.get('semantic_units', []):
        u_id = unit.get('semantic_unit_id', '')
        u_text = unit.get('semantic_core', {}).get('semantic_text', '')
        tags = unit.get('semantic_core', {}).get('domain_tags', [])
        
        interp = unit.get('unit_interpretive_layer', {})
        expl = interp.get('operational_explanation', 'غير متوفر')
        sdgs = interp.get('global_sdg_mapping', {}).get('sdg_goal', [])
        
        apps = interp.get('contemporary_application', [])
        app_text = apps[0].get('application_example', 'غير متوفر') if apps else 'غير متوفر'
        
        tags_html = "".join([f"<span class='tag-badge'>{t}</span>" for t in tags])
        sdgs_html = "".join([f"<span class='sdg-badge'>{s}</span>" for s in sdgs])
        
        html += f"""
        <div class="asu-card">
            <div style="color: #7f8c8d; font-size:13px; margin-bottom:10px; font-family: monospace;">Unit ID: {u_id}</div>
            <div class="asu-text">{u_text}</div>
            
            <div class="section-title">الوسوم المنضبطة (Tags)</div>
            <div>{tags_html}</div>
            
            <div class="section-title">التفسير الإجرائي (Low-Inference Explanation)</div>
            <div class="asu-expl">{expl}</div>
            
            <div class="section-title">التطبيق المعاصر (Contemporary Application)</div>
            <div class="asu-expl">{app_text}</div>
            
            <div class="section-title">أهداف التنمية المستدامة (SDGs)</div>
            <div>{sdgs_html}</div>
        </div>
        """
    html += "</div>"
    return html

# يمكنك إضافة دوال جديدة هنا مستقبلاً
# def template_rag_view(record): ...
def template_sdg_policy_map(matched_units, selected_sdg):
    """قالب العرض الثاني: خارطة السياسات المعاصرة وأهداف التنمية"""
    
    html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
        .policy-container {{ font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; background: #f4f6f9; padding: 20px; border-radius: 10px; max-width: 1000px; margin: auto; }}
        .sdg-header {{ background: linear-gradient(135deg, #005A9C, #00A6E0); color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}}
        .sdg-title {{ font-size: 24px; font-weight: bold; margin: 0; }}
        .sdg-count {{ font-size: 14px; background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 20px; display: inline-block; margin-top: 10px; }}
        
        .policy-card {{ background: white; border-right: 6px solid #e67e22; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        
        .contemporary-box {{ background: #fff3e0; padding: 15px; border-radius: 5px; margin-bottom: 15px; border: 1px solid #ffe0b2; }}
        .contemporary-title {{ color: #d35400; font-size: 14px; font-weight: bold; margin-bottom: 5px; }}
        .contemporary-text {{ font-size: 18px; font-weight: bold; color: #333; }}
        
        .heritage-box {{ background: #e8f5e9; padding: 15px; border-radius: 5px; margin-bottom: 15px; border: 1px solid #c8e6c9; }}
        .heritage-title {{ color: #27ae60; font-size: 14px; font-weight: bold; margin-bottom: 5px; }}
        .heritage-text {{ font-size: 17px; color: #2c3e50; font-family: Arial, sans-serif; }}
        
        .bridge-box {{ padding: 10px 15px; border-right: 4px solid #3498db; background: #ebf5fb; }}
        .bridge-title {{ color: #2980b9; font-size: 13px; font-weight: bold; margin-bottom: 5px; }}
        .bridge-text {{ font-size: 14px; color: #555; line-height: 1.6; }}
    </style>

    <div class="policy-container">
        <div class="sdg-header">
            <h1 class="sdg-title">الهدف التنموي: {selected_sdg}</h1>
            <div class="sdg-count">تم العثور على ({len(matched_units)}) توجيه نبوي يدعم هذا الهدف</div>
        </div>
    """
    
    for item in matched_units:
        hid = item['hadith_id']
        u_id = item['unit']['semantic_unit_id']
        u_text = item['unit']['semantic_core'].get('semantic_text', '')
        
        interp = item['unit'].get('unit_interpretive_layer', {})
        expl = interp.get('operational_explanation', 'غير متوفر')
        
        apps = interp.get('contemporary_application', [])
        app_text = apps[0].get('application_example', 'تطبيق عام يدعم الاستدامة') if apps else 'تطبيق عام يدعم الاستدامة'
        
        html += f"""
        <div class="policy-card">
            <div style="color: #95a5a6; font-size:12px; margin-bottom:10px;">مصدر السجل: {u_id} (من حديث {hid})</div>
            
            <div class="contemporary-box">
                <div class="contemporary-title"><i class="fas fa-lightbulb"></i> التوصية والسياسة المعاصرة (Policy Recommendation):</div>
                <div class="contemporary-text">{app_text}</div>
            </div>
            
            <div class="heritage-box">
                <div class="heritage-title"><i class="fas fa-book-open"></i> الدليل والمستند الشرعي (Prophetic Foundation):</div>
                <div class="heritage-text">"{u_text}"</div>
            </div>
            
            <div class="bridge-box">
                <div class="bridge-title">التفسير الإجرائي للربط (Operational Bridge):</div>
                <div class="bridge-text">{expl}</div>
            </div>
        </div>
        """
        
    if not matched_units:
        html += "<div style='text-align:center; padding: 30px; color:#7f8c8d;'>لا توجد توجيهات مسجلة تحت هذا الهدف في العينة الحالية.</div>"
        
    html += "</div>"
    return html
