class HtmlField(object):
    def __init__(self, **kwargs):
        self.html = ""
        if kwargs['field_type'] == "text_field":
            self.html = self.construct_text_field(kwargs["label"], kwargs["field_name"])
        elif kwargs['field_type'] == "checkbox_field":
            self.html = self.construct_checkbox(kwargs["field_id"], kwargs["value"], kwargs["label"])

    def construct_text_field(self, label, field_name):
        return '{0}:<br><input type="text" name="{1}"><br>'.format(label, field_name)
    
    def construct_checkbox(self, field_id, value, label):
        return '<label><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(field, value, label)
    
    def __str__(self):
        return self.html
    
def generate_webform(field_dict_list):
    generated_field_list = []
    for field in field_dict_list:
        try:
            generated_field_list.append(str(HtmlField(**field)))
        except Exception as e:
            print ("error: {}".format(e))
        generated_fields = "\n".join(generated_field_list)
        
    return "<form>{fields}</form>".format(fields=generated_fields)

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
