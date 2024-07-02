import os

def generate_html():
    # Base URL for the GitHub repository
    base_url = "https://github.com/aadigwe/CtrlSynSamples/raw/main/JennySamples"

    # Folders to be used
    folders = ['sent1', 'sent2', 'sent3','sent4', 'sent5', \
    'sent6', 'sent7', 'sent8','sent9', 'sent10']

    # Generate HTML content
    html_content = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Demo Page for UKIS 2024</title>
        <h1>Demo Page for UKIS 2024</h1>
        <p>In this work we aim to explore the range of prosodic diversity obtainable from Large Speech Models. The following samples are manually selected from multiple renditions to represent prosodic diversity.</p>
        <p><i>All samples created with Parler TTS, a HuggingFace Implementation of Natural language guidance of high-fidelity text-to-speech with synthetic annotations <a href="https://arxiv.org/pdf/2402.01912">Lyth & King 2024</a></i></p>
        <script>
            function loadAudioFiles() {
                const folder = document.getElementById('folder-select').value;
                const container = document.getElementById('audio-player-container');
                container.innerHTML = '';

                const audioFiles = {
    """

    for folder in folders:
        # Define audio files manually as they are on GitHub
        # This list should include the actual audio file names in each folder
        if folder == "sent1":   
            audio_files = os.listdir(os.path.join('./JennySamples', folder))      
            #audio_files = ['sent01_temp-0.3_iter-0.wav', 'sent01_temp-0.5_iter-4.wav']  # Replace with actual file names
        elif folder == "sent2":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
            #audio_files = ['sent02_temp-0.5_iter-17.wav', 'sent02_temp-0.7_iter-11.wav']  # Replace with actual file names
        elif folder == "sent3":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
            #audio_files = ['sent03_temp-1.1_iter-2.wav', 'sent03_temp-1.5_iter-37.wav']  # Replace with actual file names
        elif folder == "sent4":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent5":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent6":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent7":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent8":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent9":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))   
        elif folder == "sent10":
            audio_files = os.listdir(os.path.join('./JennySamples', folder))  
        
        html_content += f'                "{folder}": {audio_files},\n'

    html_content += """            };
            
            audioFiles[folder].forEach(function(file) {
                const audioElement = document.createElement('audio');
                audioElement.controls = true;
                const sourceElement = document.createElement('source');
                sourceElement.src = '""" + base_url + """' + '/' + folder + '/' + file;
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
        <option value="sent4">Sent4</option>
        <option value="sent5">Sent5</option>
        <option value="sent6">Sent6</option>
        <option value="sent7">Sent7</option>
        <option value="sent8">Sent8</option>
        <option value="sent9">Sent9</option>
        <option value="sent10">Sent10</option>
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
