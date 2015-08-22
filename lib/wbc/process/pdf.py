# -*- coding: utf-8 -*-
import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class Letter:

    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def appendParagraphs(self, elements, parapraphlist, fontsize, styles):
        for element in elements:
            ptext = '<font size=%i>%s: %s</font>' % (fontsize, element[0], element[1])
            parapraphlist.append(Paragraph(ptext, styles["Normal"]))
        parapraphlist.append(Spacer(1, fontsize))

    def printForm(self, form, publication):

        entities = ','.join([entity.name for entity in publication.place.entities.all()])
        fontsize = 12
        data = form.cleaned_data
        today = datetime.date.today().strftime("%d.%m.%Y")

        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        elements = []
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(name='Justify', alignment=TA_CENTER))

        elements.append(Paragraph('Stellungnahme/Vorschläge zur Änderung eines Bebauungsplanes', styles['Heading2']))
        elements.append(Spacer(1, fontsize))
        metadata = [('Bezirk(e)', entities), ('Bezeichner', publication.place.identifier), ('Stand vom:', today)]
        self.appendParagraphs(metadata, elements, fontsize, styles)
        elements.append(Paragraph('Stellungnahme', styles['Heading3']))
        ptext = '<font size=%i>%s</font>' % (fontsize, data['statement'])
        elements.append(Paragraph(ptext, styles["Normal"]))
        elements.append(Spacer(1, fontsize))

        elements.append(Paragraph('Absender', styles['Heading3']))
        ptext = '<font size=%i>Name:%s</font>' % (fontsize, data['name'])
        elements.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=%i>Strasse und Hausnummer:%s</font>' % (fontsize, data['address'])
        elements.append(Paragraph(ptext, styles["Normal"]))
        elements.append(Spacer(1, fontsize))
        ptext = '<font size=%i>Datum:%s, Unterschrift:</font>' % (fontsize, today)
        elements.append(Paragraph(ptext, styles["Normal"]))

        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()
        return pdf
