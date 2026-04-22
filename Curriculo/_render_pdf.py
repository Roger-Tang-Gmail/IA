import pypdfium2 as pdfium
import os

src = r'C:\Users\Roger\Documents\GitHub\Roger-Tang-Gmail\IA\Curriculo\Curriculo_Roger_Tang.pdf'
outdir = r'C:\Users\Roger\Documents\GitHub\Roger-Tang-Gmail\IA\Curriculo\_pdf_pages'
os.makedirs(outdir, exist_ok=True)

pdf = pdfium.PdfDocument(src)
for i, page in enumerate(pdf):
    bitmap = page.render(scale=1.4)
    img = bitmap.to_pil()
    path = os.path.join(outdir, f'page_{i+1:02d}.png')
    img.save(path, optimize=True)
    print(path, img.size)
