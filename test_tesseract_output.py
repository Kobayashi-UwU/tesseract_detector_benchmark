import pytesseract
from PIL import Image

# Load the image
image = Image.open('./groundtruth/sample_original/tha_01.png')
oem = 3
psm = 3
# Specify OEM and PSM
# Adjust OEM and PSM as needed
custom_config = f'--oem {oem} --psm {psm} -l tha'

# Get OCR data with custom configuration
data = pytesseract.image_to_data(
    image, output_type=pytesseract.Output.DICT, config=custom_config)

result = []
# Extract and print all the available data
num_boxes = len(data['level'])
for i in range(num_boxes):
    level = data['level'][i]
    page_num = data['page_num'][i]
    block_num = data['block_num'][i]
    par_num = data['par_num'][i]
    line_num = data['line_num'][i]
    word_num = data['word_num'][i]
    left = data['left'][i]
    top = data['top'][i]
    width = data['width'][i]
    height = data['height'][i]
    conf = data['conf'][i]
    text = data['text'][i]

    print(f'Level: {level}, Page: {page_num}, Block: {block_num}, Paragraph: {par_num}, Line: {line_num}, Word: {word_num}, '
          f'Bounding Box: ({left}, {top}, {width}, {height}), Confidence: {conf}, Text: "{text}"')
    # if conf > 30:
    # result.append([left, top, width, height, conf, text])

print(result)

# Level: 1, Page: 1, Block: 0, Paragraph: 0, Line: 0, Word: 0, Bounding Box: (0, 0, 592, 162), Confidence: -1, Text: ""
# Level: 2, Page: 1, Block: 1, Paragraph: 0, Line: 0, Word: 0, Bounding Box: (58, 43, 534, 103), Confidence: -1, Text: ""
# Level: 3, Page: 1, Block: 1, Paragraph: 1, Line: 0, Word: 0, Bounding Box: (58, 43, 534, 103), Confidence: -1, Text: ""
# Level: 4, Page: 1, Block: 1, Paragraph: 1, Line: 1, Word: 0, Bounding Box: (58, 43, 244, 40), Confidence: -1, Text: ""
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 1, Word: 1, Bounding Box: (58, 43, 38, 40), Confidence: 31, Text: "®"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 1, Word: 2, Bounding Box: (138, 45, 164, 29), Confidence: 82, Text: "ChatGPT"
# Level: 4, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 0, Bounding Box: (140, 110, 452, 36), Confidence: -1, Text: ""
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 1, Bounding Box: (140, 110, 20, 29), Confidence: 82, Text: "It"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 2, Bounding Box: (170, 118, 115, 21), Confidence: 95, Text: "seems"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 3, Bounding Box: (295, 110, 69, 29), Confidence: 96, Text: "that"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 4, Bounding Box: (374, 110, 56, 29), Confidence: 96, Text: "the"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 5, Bounding Box: (441, 110, 100, 36), Confidence: 67, Text: "script"
# Level: 5, Page: 1, Block: 1, Paragraph: 1, Line: 2, Word: 6, Bounding Box: (553, 110, 25, 29), Confidence: 56, Text: "is"


# "Level" คือระดับของลำดับของข้อความที่ตรวจพบ
# 1 แทนหน้ากระดาษ
# 2 แทนบล็อกของข้อความ
# 3 แทนย่อหน้าภายในบล็อก
# 4 แทนบรรทัดภายในย่อหน้า
# 5 แทนคำในบรรทัด

# "Page Number (page_num)" เลขหน้าที่พบข้อความ ในตัวอย่างเป็นเสมอที่ 1 แสดงว่าข้อความทั้งหมดมาจากหน้าแรกของเอกสาร

# "Block Number (block_num)" คือหมายเลขของบล็อกภายในหน้า เป็นพื้นที่ที่มีข้อความอยู่ ในตัวอย่างเลขของบล็อกเพิ่มขึ้นสำหรับส่วนข้อความที่แตกต่างกัน

# "Paragraph Number (par_num)" คือหมายเลขของย่อหน้าภายในบล็อก ย่อหน้าคือส่วนข้อความที่แยกกันด้วยการเปลี่ยนบรรทัด ในตัวอย่างนี้มีการเพิ่มค่าเมื่อมีย่อหน้าใหม่

# "Line Number (line_num)" หมายถึงหมายเลขบรรทัดภายในย่อหน้า บรรทัดคือส่วนของข้อความที่แยกกันด้วยการเปลี่ยนบรรทัดหรือสัญลักษณ์ที่เห็น ในตัวอย่างมันเพิ่มขึ้นสำหรับแต่ละบรรทัดของข้อความ

# "Word Number (word_num)" หมายถึงหมายเลขคำภายในบรรทัด คำคือลำดับของตัวอักษรที่แยกกันด้วยช่องว่างหรือเครื่องหมายวรรคตอน ในตัวอย่างมันเพิ่มขึ้นสำหรับแต่ละคำในบรรทัด

# "Bounding Box (left, top, width, height)" หมายถึงพิกัดและขนาดของกล่องครอบที่ล้อมรอบข้อความที่ตรวจพบ มันระบุตำแหน่งและขนาดของพื้นที่ข้อความภายในภาพ ในตัวอย่างมันได้แสดงให้เห็นเป็น (left, top, width, height) สำหรับแต่ละส่วนข้อความ

# "Confidence (conf)" หมายถึงคะแนนความมั่นใจสำหรับข้อความที่ตรวจพบ มันบ่งบอกถึงระดับความมั่นใจของเครื่อง OCR ในความแม่นยำของข้อความที่ตรวจพบ ค่าความมั่นใจที่สูงมักแสดงถึงความแม่นยำที่สูงขึ้น ในตัวอย่างมันเป็นคะแนนความมั่นใจที่เริ่มจาก 0 ถึง 100

# "Text" หมายถึงข้อความที่ตรวจพบจริง ฟิลด์นี้ประกอบด้วยข้อความที่จำแนกได้ว่าข้อความจริงที่ Tesseract OCR ตรวจพบในกล่องตรวจหาข้อความที่เกี่ยวข้อง ในตัวอย่างนี้มันรวมถึงคำและตัวอักษรที่จำแนกได้
