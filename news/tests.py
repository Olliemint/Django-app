from django.test import TestCase
from .models import Editor,Article,Tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_editor = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_editor,Editor))
    
    
    # Testing Save Method
    def test_save_method(self):
        self.new_editor.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
        
    # Testing delete method
    def test_delete_method(self):
        self.new_editor.delete_editor()
        
        editor_len= Editor.objects.count()
        self.assertEqual(Editor.objects.count(), editor_len- 1)