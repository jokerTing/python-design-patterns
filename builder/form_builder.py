from abc import ABCMeta, abstractmethod

class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None
    
    def set_builder(self, builder):
        self._builder = builder
    
    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object

'''
class ConcreteDirector(Director):
    pass
'''
class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)
    
    def construct(self, field_list):
        for field in field_list:
            if field["type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["type"] == "button":
                self._builder.add_button(field)

class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object
    
    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass

'''
class ConcreteBuilder(Builder):
    pass
'''
class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()
    
    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(
                field_dict["label"], field_dict["name"]
            )
        )
    
    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            '<label><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
                checkbox_dict["id"], checkbox_dict["value"], checkbox_dict["label"]
            )
        )
    
    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(
                button_dict['text']
            )
        )

'''
class Product(object):
    def __init__(self):
        pass
    def __repr_(self):
        pass
'''
class HtmlForm(object):
    def __init__(self):
        self.field_list = []
    def __repr__(self):
        return "<form>{}</form>".format("".join(self.field_list))

if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)

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
        },
        {
            "type": "button",
            "text": "DONE"
        }
    ]
    director.construct(field_list)
    with open("builder/form_file.html", 'w') as f:
        f.write(
            "<html><body>{0!r}</body></html>".format(
                director.get_constructed_object()
            )
        )