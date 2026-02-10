# RAG Over Audio

RAG Over Audio is a small pipeline that transcribes an audio file, stores transcript chunks in a Chroma vector database, and answers questions by retrieving relevant chunks and prompting a local LLM (Ollama).

<img src="/images/assembly-audio-rag.gif" alt="description" style="width:100%; height:auto;" />

## Features

- Whisper-based transcription for audio files
- Chunking and ingestion into ChromaDB
- Retrieval-augmented answering via Ollama local API

## Project Structure

- main.py: Orchestrates transcription, ingestion, and Q&A
- transcribe.py: Transcribes audio using Whisper
- ingest.py: Chunks text and ingests into ChromaDB
- query.py: Retrieves chunks and queries Ollama
- audio/: Place audio files here
- db/: ChromaDB persistence folder

## Requirements

- Python 3.9+ (recommended)
- FFmpeg installed (needed by Whisper)
- Ollama running locally (for Q&A)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update these values in main.py as needed:

- audio_path: Path to the audio file (default: audio/pure-tone.wav)
- ffmpeg_path: Full path to ffmpeg.exe on Windows

Example ffmpeg path used in the code:

```
C:\Users\eiman.tahir\Downloads\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe
```

## Usage

Run the end-to-end pipeline:

```bash
python main.py
```

You will be prompted to enter a question about the audio after transcription and indexing completes.

## Notes

- The query step calls the Ollama API at http://localhost:11434/api/generate.
- The default LLM model name in query.py is mistral. Change it if your local model name differs.
- Transcription model defaults to Whisper base. You can change model_name in transcribe.py.

