from django.test import TestCase
from .models import todo
from .views import completed
from .add_task import PostForm
from django.utils import timezone

class TodoTestCase(TestCase):
    def setUp(self):
        todo.objects.create(username="jsno", name="jon", description="prototype due");
        todo.objects.create(username="gmon", name="gabriella", description="deployment due");
        todo.objects.create(username="tbol", name="troy", description="hci due");
        todo.objects.create(username="dtar", name="daeni", description="buy milk");
        todo.objects.create(username="jhua", name="jessica", description="buy candy");
        todo.objects.create(username="bbec", name="brooklyn", description="pay rent");
        todo.objects.create(username="gmon", name="gabriella", description="organise bday party");
        todo.objects.create(username="jhua", name="jessica", description="movies");

    def test_todolist_exists(self):
        """Check if the todolist exists"""
        js = todo.objects.get(username="jsno", description="prototype due");
        gm = todo.objects.get(username="gmon", description="deployment due");
        jh = todo.objects.get(username="jhua", description="movies");
        gm1 = todo.objects.get(username="gmon", description="organise bday party");
        self.assertEqual(js.description, "prototype due");
        self.assertEqual(gm.description, "deployment due");
        self.assertEqual(jh.description, "movies");
        self.assertEqual(gm1.description, "organise bday party");

    def test_todolist_not_completed(self):
        """Check if the todolist is not completed yet"""
        js = todo.objects.get(username="jsno", description="prototype due");
        gm = todo.objects.get(username="gmon", description="deployment due");
        jh = todo.objects.get(username="jhua", description="movies");
        gm1 = todo.objects.get(username="gmon", description="organise bday party");
        self.assertEqual(js.completed, False);
        self.assertEqual(gm.completed, False);
        self.assertEqual(jh.completed, False);
        self.assertEqual(gm1.completed, False);
        
    def test_todolist_completed(self):
        """ACheck if the todolist is completed"""
        jh = todo.objects.get(username="jhua", description="movies");
        jh.completed = True;
        jh.save();
        gm = todo.objects.get(username="gmon", description="organise bday party");
        gm.completed = True;
        gm.save();

        self.assertEqual(jh.completed, True);
        self.assertEqual(gm.completed, True);

    def test_valid_form(self):
        i1 = todo.objects.create(username='dtar', name='Foo', description='Bar');
        i2 = todo.objects.create(username='tbol', name='Sky', description='High', date=timezone.now());
        i3 = todo.objects.create(username='bbec', name='Photo', description='Graph', date=timezone.now());
        data1 = {'name': i1.name, 'description': i1.description, 'date': i1.date}
        data2 = {'name': i2.name, 'description': i2.description, 'date': i2.date}
        data3 = {'name': i3.name, 'description': i3.description, 'date': i3.date}
        form1 = PostForm(data=data1);
        form2 = PostForm(data=data2);
        form3 = PostForm(data=data3);
        self.assertTrue(form1.is_valid());
        self.assertTrue(form2.is_valid());
        self.assertTrue(form3.is_valid());

    def test_invalid_form(self):
        i1 = todo.objects.create(username='dtar', name='Foo');
        i2 = todo.objects.create(username='dtar', description='Bar', date=timezone.now());
        data1 = {'name': i1.name, 'description': i1.description, 'date': i1.date}
        data2 = {'name': i2.name, 'description': i2.description, 'date': i2.date}
        form1 = PostForm(data=data1);
        form2 = PostForm(data=data2);
        self.assertFalse(form1.is_valid());
        self.assertFalse(form2.is_valid());




            