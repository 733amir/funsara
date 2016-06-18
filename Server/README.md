
This part of project is about a tool that manages requests and database.

**Attention**: All UPPERCASE strings in this description will be changed with the proper value that they are describing.

# 1. Files structure

```
root-of-project/
|-- batch.py
|-- database.py
|-- server.py
|-- videos /
    |-- VIDEO-ID /
        |-- THUMBNAIL-IMAGE-ABOUT-THE-VIDEO
        |-- BLURRED-THUMBNAIL-IMAGE-ABOUT-THE-VIDEO
        |-- VIDEO-FILE
```

## 1.1. server.py

### 1.1.1 Requests

#### 1.1.1.1. GET `/api/versions`

Returns a JSON object bellow, where **APP-VERSION** is the lowest version of android application that user should have.

```
{
    "lastBatchNumber" : LAST-BATCH-NUMBER
    "appVersion" : APP-VERSION
}
```

#### 1.1.1.2. GET `/api/batch?number=BATCH-NUMBER`

Returns a JSON array that contains objects like bellow. These objects contain information about videos in the batch.  

```
{
    "url": URL-OF-THUMBNAIL-PICTURE-ABOUT-THE-VIDEO,
    "blurredUrl": URL-OF-BLURED-THUMBNAIL-PICTURE-ABOUT-THE-VIDEO,
    "titleOfStory" : TITLE-OF-THE-VIDEO,
    "smallDetailOfStory": SMALL-DESCRIPTION-ABOUT-THE-VIDEO,
    "fullDetailOfStory": FULL-DESCRIPTION-ABOUT-THE-VIDEO,
    "time": LENGTH-OF-THE-VIDEO,
    "videoUrl": URL-OF-THE-VIDEO
}
```

## 1.2. database.py

### 1.2.1. Tables

**batches**:

|id|number|video_id|
|--|------|--------|

**videos**:

|id|img_url|blurred_img_url|title|short_detail|long_detail|time|video_url|
|--|-------|---------------|-----|-----------------|----------------|----|---------|


## 1.3. batch.py
