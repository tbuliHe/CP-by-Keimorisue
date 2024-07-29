import os

# 读取文件列表
with open('../pics_list.txt', 'r') as f:
    pics_files = f.read().splitlines()

with open('../png_list.txt', 'r') as f:
    png_files = f.read().splitlines()

# 匹配并生成HTML内容
items = []
for png in png_files:
    for pic in pics_files:
        png_base = os.path.splitext(png)[0].replace('_cp', '')
        pic_base = os.path.splitext(pic)[0]
        if png_base == pic_base:
            item = f"""
            <div class="item">
                <div class="images">
                    <img src="../PNG_format/{png}" alt="{png_base} cp" onclick="showModal(this)">
                    <img src="../pics/{pic}" alt="{pic_base}" onclick="showModal(this)">
                </div>
                <div class="file-name">{pic_base}</div>
            </div>
            """
            items.append(item)
            break

html_content = '\n'.join(items)

# 输出到HTML文件
output_html = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>森魔鬼的cp集</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        .search-bar {{
            margin-bottom: 20px;
        }}
        .container {{
            display: flex;
            flex-wrap: wrap;
        }}
        .item {{
            width: 40%;
            margin: 1%;
            border: 1px solid #ddd;
            padding: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }}
        .images {{
            display: flex;
            justify-content: space-between;
        }}
        .images img {{
            width: 40%;
            transition: transform 0.2s;
            cursor: pointer;
        }}
        .images img:hover {{
            transform: scale(1.1);
        }}
        .file-name {{
            text-align: center;
            margin-top: 10px;
            font-weight: bold;
        }}
        .modal {{
            display: none;
            position: fixed;
            z-index: 1;
            padding-top: 60px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.9);
        }}
        .modal-content {{
            margin: auto;
            display: block;
            width: 80%;
            max-width: 700px;
        }}
        .modal-content, #caption {{
            -webkit-animation-name: zoom;
            -webkit-animation-duration: 0.6s;
            animation-name: zoom;
            animation-duration: 0.6s;
        }}
        @-webkit-keyframes zoom {{
            from {{-webkit-transform: scale(0)}}
            to {{-webkit-transform: scale(1)}}
        }}
        @keyframes zoom {{
            from {{transform: scale(0)}}
            to {{transform: scale(1)}}
        }}
        .close {{
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
        }}
        .close:hover,
        .close:focus {{
            color: #bbb;
            text-decoration: none;
            cursor: pointer;
        }}
    </style>
    <script>
        function searchFiles() {{
            const input = document.getElementById('search').value.toLowerCase();
            const items = document.getElementsByClassName('item');
            Array.from(items).forEach(item => {{
                const fileName = item.getElementsByClassName('file-name')[0].textContent.toLowerCase();
                if (fileName.includes(input)) {{
                    item.style.display = '';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }}

        function showModal(img) {{
            const modal = document.getElementById('myModal');
            const modalImg = document.getElementById('img01');
            const captionText = document.getElementById('caption');
            modal.style.display = 'block';
            modalImg.src = img.src;
            captionText.innerHTML = img.alt;
        }}

        function closeModal() {{
            const modal = document.getElementById('myModal');
            modal.style.display = 'none';
        }}
    </script>
</head>
<body>
    <h1>森魔鬼的cp集</h1>
    <div class="search-bar">
        <input type="text" id="search" onkeyup="searchFiles()" placeholder="Search Files...">
    </div>
    <div class="container">
        {html_content}
    </div>

    <div id="myModal" class="modal">
        <span class="close" onclick="closeModal()">&times;</span>
        <img class="modal-content" id="img01">
        <div id="caption"></div>
    </div>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)
