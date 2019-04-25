def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_text_field(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkbox(field_dict)
        generated_field_list.append(field_html)
    generated_fields = "\n".join(generated_field_list)
    return "<form>{fields}</form>".format(fields=generated_fields)

def generate_text_field(text_field_dict):
    return '{0}:<br><input type="text" name="{1}"><br>'.format(
        text_field_dict["label"], text_field_dict["name"])

def generate_checkbox(checkbox_dict):
    return '<label><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
        checkbox_dict["id"], checkbox_dict["value"], checkbox_dict["label"])

def build_html_form(field_list):
    with open("builder/form_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(generate_webform(field_list))
        )
if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "value": 1,
            "label": "Check for me"
        },
        {
            "type": "text_field",
            "label": "Another Text field",
            "name": "text_field2"
        }
    ]
    build_html_form(field_list)