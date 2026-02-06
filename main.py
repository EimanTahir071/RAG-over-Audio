from transcribe import transcribe_audio
from ingest import ingest_text_to_chroma
from query import query_audio_knowledge


def main() -> None:
    audio_path = "audio/pure-tone.wav"

    print("Transcribing...")
    transcript = transcribe_audio(audio_path)

    print("Indexing transcript...")
    ingested = ingest_text_to_chroma(transcript)
    print(f"Indexed {ingested} chunks.")

    print("Ask a question about the audio:")
    user_query = input(">> ").strip()
    if not user_query:
        print("No question provided.")
        return

    answer = query_audio_knowledge(user_query)
    print("\nAnswer:", answer)


if __name__ == "__main__":
    main()
