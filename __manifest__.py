{
    'name': 'Multiuser Todo Application',
    'description': 'Extension de l\'application todo application',
    'author': 'Christian Rakotomalala',
    'data': [
        './views/todo_task.xml',
        './security/todo_access_rules.xml'
        ],
    'depends': ['todo_application', 'mail'],
    'demo': ['data/todo.task.csv', 'data/todo_data.xml'],
}
