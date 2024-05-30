import os
from PIL import Image
import xml.etree.ElementTree as ET
import pandas as pd

def parse_annotation_txt(annotation_file):
    with open(annotation_file, "r") as f:
        annotations = [line.strip().split(",") for line in f.readlines()]
    return annotations


if __name__ == '__main__':
    images = []
    annotations = []

    for dirpath, dirnames, filenames in os.walk("simpsons_dataset"):
        for filename in filenames:
            if filename.endswith(".jpg"):
                images.append(os.path.join(dirpath, filename))

        annotation_file = os.path.join(dirpath, "annotation.xml")
        if os.path.exists(annotation_file):
            annotations.append(annotation_file)

    annotations_data = []

    for annotation_file in annotations:
        annotations_data += parse_annotation_txt(annotation_file)

    df = pd.DataFrame({
        "image_path": images,
        "annotations": annotations_data
    })

    df["width"] = df["image_path"].apply(lambda x: Image.open(x).width)
    df["height"] = df["image_path"].apply(lambda x: Image.open(x).height)

    print(df.values[0:10])

