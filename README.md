# Market Surveillance Android App

This Android application, named "Market Surveillance," is designed to streamline the workflow of market inspections. The app, written in Kotlin, facilitates the process of documenting and recording information about products inspected in markets.

## Project Overview

The primary functionalities of the app include:

1. **Image Text Recognition**: Users can capture photos of products and use ML Kit Text Recognition v2 to extract text information. This data is then populated into fields such as product name, origin, etc., and can be uploaded to a Google Sheet for archival purposes.

2. **Google Drive Integration**: The app integrates with Firebase to upload captured images directly to Google Drive for storage.

## Purpose

The motivation behind developing this app stems from the need to streamline the inspection process. With approximately 6000 products inspected annually, automating data entry through image recognition significantly reduces manual transcription time. Additionally, storing data in cloud-based solutions ensures accessibility and facilitates further analysis.

## File Descriptions

1. **MainActivity.kt**: This serves as the home page of the app, featuring buttons for "Market Inspection" and "Upload Photos to Cloud." The former redirects to `ProductInfo.kt`, where users can manually input data or utilize the image recognition feature. Selecting "Take Photo" leads to `NextActivity.kt`.

2. **ProductInfo.kt**: This activity displays fields for comprehensive product information such as name, manufacturer/importer details, and address.

3. **NextActivity.kt**: Utilizes Google ML Kit for text recognition. Extracted text is populated into predefined fields, and a "Submit" button uploads the data to Google Sheets.

4. **TextRecognitionProcessor**: Implements the logic for text recognition using Google ML Kit.

5. **UploadActivity**: Implements the logic for uploading files to Google Drive.

## Design Considerations

1. **Data Storage**: Choosing between Firebase and Google Sheets for data storage was deliberated. Google Sheets was selected due to its compatibility with the existing database system utilized by the organization.

2. **Google Drive Integration**: Initially, attempts were made to directly integrate with Google Drive API. However, due to stricter authentication requirements for native apps, Firebase was adopted as an intermediary for successful integration.

3. **Text Recognition Model**: ML Kit was chosen for its ease of integration and suitability for mobile applications. Besides, it can recognize text in any Chinese, Devanagari, Japanese, Korean and Latin character set. Although alternatives like Google Docs offer text recognition capabilities, ML Kit's dedicated SDK for mobile development provided a more streamlined solution.

## References

- [Integrate Google Drive For Backup data on android Kotlin Jetpack Compose](https://medium.com/@salman.alamoudi95/integrate-google-drive-for-backup-data-on-android-kotlin-jetpack-compose-e92cff32f71f)
- [ML Kit Quickstart](https://github.com/googlesamples/mlkit)
- ChatGPT



------
# Deploy LINE Bot Python Examples on Render

This repo can be used to deploy python examples in the [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples) on [Render](https://render.com/).
## Prerequisites
Make sure you have the following:
- A dedicated [Messaging API channel](https://developers.line.biz/en/docs/messaging-api/getting-started/) for your bot.
- A [Render account](https://dashboard.render.com/register) that doesn't require credit card to sign up.

## Deployment
1. Fork this repo.
2. Update `render.yaml` to comment/uncomment the services of LINE bot examples you want to deploy.
3. Cieck to deploy
   
   [![Deploy to Render](http://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

4. You will be prompted to input LINE channel secret and [access token](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/). You can find them on the [LINE Developers Console](https://developers.line.biz/console/). Channel secret is on the channel's `Basic settings` tab. Channel access token is on the channel's `Messaging API` tab.
5. Once the bot servcie is live, find the service `onrender` URL (e.g., `https://line-bot-python-<something unique>.onrender.com`) on the Dashboard. Append `/callback` to the service URL to build the webhook URL (e.g., `https://line-bot-python-<something unique>.onrender.com/callback`). Paste the webhook URL to the `Webhook settings` section on the LINE channel's `Messaging API` tab on the [LINE Developers Console](https://developers.line.biz/console/). Also enable `Use webhook` on the same section.
6. Add the LINE Official Account associated with your bot as a friend on LINE by scanning the QR code on the `Messaging API` tab of your channel settings on the [LINE Developers Console](https://developers.line.biz/console/).
7. That's it. Send your LINE Official Account a text message on LINE and confirm that it responds with the same message.

## Notes
- If your LINE bot app files are in the same repo as `render.yaml`, you don't need to specify `repo` in the `render.yaml`. You can find more information in the [Render Blueprint spec](https://render.com/docs/blueprint-spec#repo--branch).
