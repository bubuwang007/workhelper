import docx

document = docx.Document()
paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.', style='List Bullet')
paragraph.style = 'List Bullet'

document.save('demo.docx')