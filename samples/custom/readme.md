# 2021 차로위반영상데이터 활용 AI 해커톤

**TrafficFlow Team**

Mask R-CNN 모델 개발 custom directory

#
![ezgif com-gif-maker](https://user-images.githubusercontent.com/66053034/145726143-95184060-0572-4388-9964-de8c35fc6913.gif)
#

* custom.py
> custom model에 대한 config와 class 설정이 들어있는 파일

* anno2via.py
> 제공된 dataset의 annotation을 VIA format으로 변환하는 코드

* tvai-mask-rcnn-training.ipynb
> custom model에 대한 training을 하고 h5를 logs directory에 저장하는 노트북

* test-visualize.ipynb
> 학습된 model을 시각화 하여 test하는 노트북
> ![tvai121](https://user-images.githubusercontent.com/66053034/145727340-e74d24b4-4f29-4fea-b203-b3239d21ba72.png)
