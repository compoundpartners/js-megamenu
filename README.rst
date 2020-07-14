JumpSuite Megamenu
====


You can use page extention in template

{% if request.toolbar.edit_mode and request.current_page.megamenuextension.show_megamenu %}
    {% placeholder megamenu %}
{% endif %}
