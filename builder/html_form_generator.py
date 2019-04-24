def generate_webform(text_field_list, checkbox_field_list):
    generate_field = "\n".join(
        map(
            lambda x:'{0}:<br><input type="text" name="{0}"><br>'.format(x),# input text 
            text_field_list
        )
    )

    generate_field += "\n".join(
        map(
            lambda x:'<label><input type="checkbox" id="{0}" value="{0}">{0}<br>'.format(x),# input checkbox
            checkbox_field_list
        )
    )
    return "<form>{fields}</form>".format(fields=generate_field)

def build_html_form(text_field_list, checkbox_field_list):
    with open("builder/form_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(generate_webform(text_field_list, checkbox_field_list))
        )
if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html_form(text_fields, checkbox_fields)