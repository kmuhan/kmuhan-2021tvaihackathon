import os
import json
import shutil

'''
[[1304, 'BLUE'], 
[37, 'SHOULDER'], 
[122, 'WHITE'], 
[3, 'YELLOW'], 
[13, 'BLUE'], 
[440, 'WHITE'], 
[11, 'YELLOW'], 
[58, 'BLUE'], 
[522, 'SHOULDER'], 
[43, 'WHITE']]

BLUE = 1375
WHITE = 605
YELLOW = 14
SHOULDER = 559
SUM = 2553
'''

image_folder_path = os.path.abspath('IMAGE')
annotation_folder_path = os.path.abspath('ANNOTATION')
via_path = os.path.abspath('dataset/train/via_region_data.json')

# Loop file directory
lis = []

jj = {

}
jjj = {

}
for f in os.listdir(annotation_folder_path):
    if f == 'desktop.ini':
        continue
    for g in os.listdir(os.path.join(annotation_folder_path, f)):
        if g == 'desktop.ini':
            continue
        for h in os.listdir(os.path.join(annotation_folder_path, f, g)):
            if h == 'desktop.ini':
                continue

            # Open json file
            with open(os.path.join(annotation_folder_path, f, g, h), "r") as file:
                anno = json.load(file)
                # 데이터 아이디 저장
                dataID = anno['dataID']
                # filename 소스 밸류 저장
                anno = anno['data_set_info']
                sourceValue = anno['sourceValue']

                data = {
                    "fileref": "",
                    "size": 2073600,
                    "filename": os.path.basename(sourceValue),
                    "base64_img_data": "",
                    "file_attributes": {},
                    "regions": {

                    }
                }

                for o in anno['data']:
                    objectID = o['objectID']

                    value = o['value']
                    all_points_x = []
                    all_points_y = []
                    for p in value["points"]:
                        all_points_x.append(p['x'])
                        all_points_y.append(p['y'])

                    metainfo = value['metainfo']
                    object_Label = value['object_Label']
                    extra = value['extra']

                    data['regions'][objectID] = {
                        "shape_attributes": {
                            "name": "polygon",
                            "all_points_x": all_points_x,
                            "all_points_y": all_points_y
                        },
                        "region_attributes": {
                            "metainfo": metainfo,
                            "object_Label": object_Label,
                            "extra": extra
                        }
                    }
                lis.append([dataID, data, sourceValue])

count = 0
for i in range(len(lis)):
    if i % 5 == 0:
        try:
            shutil.copyfile(lis[i][2], os.path.join('dataset/val', os.path.basename(lis[i][2])))
            jjj[lis[i][0]] = lis[i][1]
        except FileNotFoundError:
            pass
    else:
        try:
            shutil.copyfile(lis[i][2], os.path.join('dataset/train', os.path.basename(lis[i][2])))
            jj[lis[i][0]] = lis[i][1]
        except FileNotFoundError:
            pass
    count += 1
    print("copying: ", count)

with open(via_path, "w") as outfile:
    json.dump(jj, outfile, indent=4)

with open('dataset/val/via_region_data.json', 'w') as outfile:
    json.dump(jjj, outfile, indent=4)

