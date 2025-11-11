thonimport cairosvg
import os

def convert_svg_to_png(svg_path, png_path):
    cairosvg.svg2png(url=svg_path, write_to=png_path)
    print(f"Converted {svg_path} to {png_path}")

def convert_svgs_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".svg"):
            svg_path = os.path.join(folder_path, file_name)
            png_path = os.path.join(folder_path, file_name.replace(".svg", ".png"))
            convert_svg_to_png(svg_path, png_path)