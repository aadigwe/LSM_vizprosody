import os

def generate_html():
    # Base folders
    folders = ['sent1', 'sent2', 'sent3']

    # Generate HTML content
    html_content = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Demo Page for UKIS 2024</title>
        <h1>Demo Page for UKIS 2024</h1>
        <p>In this work we aim to explore the range of prosodic diversity obtainable from Large Speech Models</p>
        <p><i>All samples created with Parler TTS, a HuggingFace Implementation of Natural language guidance of high-fidelity text-to-speech with synthetic annotations <a href="https://arxiv.org/pdf/2402.01912">Lyth & King 2024</a></i></p>
        <script>
            function loadAudioFiles() {
                const folder = document.getElementById('folder-select').value;
                const container = document.getElementById('audio-player-container');
                container.innerHTML = '';

                const audioFiles = {
    """

    for folder in folders:
        audio_files = [os.path.join('/Users/adaezeadigwe/Desktop/GithubPages/LSM_vizprosody/JennySamples',folder,f) for f in os.listdir(os.path.join('JennySamples',folder)) if f.endswith('.mp3') or f.endswith('.wav')]
        print(audio_files)
        html_content += f'                "{folder}": {audio_files},\n'

    html_content += """            };
            
            audioFiles[folder].forEach(function(file) {
                const audioElement = document.createElement('audio');
                audioElement.controls = true;
                const sourceElement = document.createElement('source');
                sourceElement.src = '/Users/adaezeadigwe/Desktop/GithubPages/LSM_vizprosody/JennySamples' + folder + '/' + file;
                sourceElement.type = 'audio/mpeg';
                audioElement.appendChild(sourceElement);
                container.appendChild(audioElement);
                container.appendChild(document.createElement('br'));
            });
        }
        
        window.onload = function() {
            loadAudioFiles();  // Load initial audio files
        }
    </script>
</head>
<body>
    <select id="folder-select" onchange="loadAudioFiles()">
        <option value="sent1">Sent1</option>
        <option value="sent2">Sent2</option>
        <option value="sent3">Sent3</option>
    </select>
    <div id="audio-player-container">
    </div>
</body>
</html>
"""

    with open('index.html', 'w') as file:
        file.write(html_content)

def main():
    generate_html()
    print("HTML file has been generated successfully!")

if __name__ == "__main__":
    main()
