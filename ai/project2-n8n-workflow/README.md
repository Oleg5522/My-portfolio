# AI-Powered Lecture Accessibility Workflow

An n8n automation workflow that transcribes English audio lectures, translates them into Ukrainian, and generates an audio summary — built as a final project for an AI Essentials course.

## The problem it solves

Missing a lecture is costly when the material is complex and the language is not your native one. This workflow was built out of a personal need: after missing several AI course classes due to surgery and travel, I needed a way to process recorded English lectures and consume the content in Ukrainian.

## What the workflow does

1. **Reads** an `.mp3` audio file from a local directory
2. **Transcribes** the English audio to text using OpenAI Whisper (`whisper-1`)
3. **Translates** the transcription into Ukrainian using OpenAI GPT (`gpt-3.5-turbo`)
4. **Summarizes** the Ukrainian translation into a concise summary (under 4000 characters)
5. **Generates audio** narration of the Ukrainian summary using OpenAI TTS (`tts-1`)
6. **Saves** the audio summary as an `.mp3` file to a local output directory

## Technologies

- [n8n](https://n8n.io) — workflow automation platform (self-hosted via Docker)
- OpenAI API — Whisper (transcription), GPT-3.5-turbo (translation & summarization), TTS (audio generation)
- Docker Desktop (WSL2 backend) — local n8n environment
- Windows host with volume mounting for file access

## How to run

### Prerequisites
- Docker Desktop installed
- OpenAI API key

### Start n8n with file access
```bash
docker run -it --rm --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  -v C:\N8N_Audio:/mnt/host_audio \
  n8nio/n8n
```

### Import the workflow
1. Open n8n at `http://localhost:5678`
2. Go to Workflows → Import
3. Upload `My_workflow061025_17_35.json`
4. Add your OpenAI API key in the credentials settings
5. Place your `.mp3` lecture file in `C:\N8N_Audio\`
6. Update the file path in the "Read Audio File" node
7. Run the workflow manually

### Output
The Ukrainian audio summary will be saved to `C:\N8N_Audio\output_results\`

## Challenges encountered

- **Docker volume mounting** — file access from the n8n container required explicit WSL2 volume syntax, which took significant troubleshooting
- **OpenAI API instability** — encountered 502 and connection errors during development due to OpenAI service outages; resolved by retrying after the API returned to operational status
- **TTS character limit** — OpenAI TTS has a 4096-character limit per request; addressed by summarizing the translation before audio generation rather than narrating the full text
- **Translation language bug** — early versions produced English-to-English output due to incorrect prompt configuration; fixed by specifying the target language explicitly in the GPT prompt

## Project results

- **Input:** 25-minute English audio lecture segment (24.2 MB `.mp3`)
- **Output:** Ukrainian audio summary (~700–800 KB `.mp3`, approximately 3–5 minutes)
- **Grade:** 13/15

## Future enhancements

- Split long audio files into chunks to handle lectures over 25 MB (Whisper API limit)
- Generate SRT subtitle files with timestamps for video synchronization
- Automate video-to-audio extraction using FFmpeg
- Support full Ukrainian narration of the complete translation, not just the summary

## Notes

This is a final project completed as part of an AI Essentials course at CanCode Communities, New York.