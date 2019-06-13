{
    'name': "Online Exam / Test / Quiz",
    'version': "1.0.2",
    'author': "Bassam Infotech LLP",
    'category': "Tools",
    'support': "info@bassaminfotech.com",
    'summary': "Online Exam / Test / Quiz",
    'license':'GPL-3',
    'data': [
        'data/mail.template.csv',
        'data/res.groups.csv',
        'security/ir.model.access.csv',
        'views/etq_exam.xml',
        'views/exam_templates.xml',
        'views/etq_results.xml',
        'views/etq_exam_share.xml',
        'report/exam_test_view.xml',
        'report/exam_report_certificate.xml',
    ],
    'demo': [],
    'images':[
    'static/description/2.jpg',
    ],
    'depends': ['website', 'mail'],
    'installable': True,
}