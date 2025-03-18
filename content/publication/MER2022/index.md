---
title: "Detecting Music-Induced Emotion Based on Acoustic Analysis and Physiological Sensing: A Multimodal Approach"
authors:
- Xiao Hu
- admin
- Ruilun Liu
date: "2022-09-18T00:00:00Z"
doi: "https://doi.org/10.3390/app12189354"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-09-18T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Applied Sciences*
publication_short: In *Applied Sciences*

abstract: The subjectivity of listeners’ emotional responses to music is at the crux of optimizing emotion-aware music recommendation. To address this challenge, we constructed a new multimodal dataset (“HKU956”) with aligned peripheral physiological signals (i.e., heart rate, skin conductance, blood volume pulse, skin temperature) and self-reported emotion collected from 30 participants, as well as original audio of 956 music pieces listened to by the participants. A comprehensive set of features was extracted from physiological signals using methods in physiological computing. This study then compared performances of three feature sets (i.e., acoustic, physiological, and combined) on the task of classifying music-induced emotion. Moreover, the classifiers were also trained on subgroups of users with different Big-Five personality traits for further customized modeling. The results reveal that (1) physiological features contribute to improving performance on valence classification with statistical significance; (2) classification models built for users in different personality groups could sometimes further improve arousal prediction; and (3) the multimodal classifier outperformed single-modality ones on valence classification for most user groups. This study contributes to designing music retrieval systems which incorporate user physiological data and model listeners’ emotional responses to music in a customized manner.


# Summary. An optional shortened abstract.
summary: _Applied Sciences_, 12(18), 9354.

tags:
- Multimodal recognition
- Music retrieval
- Physiological measures
- Sound and music computing
- Music emotion recognition
featured: false

links:
# - name: Slide
#   url: media/LAK21/slide.pdf
url_pdf: 
# url_code: '#'
# url_dataset: '#'
# url_poster: ''
url_project: ''
url_slides: ''
# url_source: '#'
# url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: 
- music-emotion-recognition

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---


