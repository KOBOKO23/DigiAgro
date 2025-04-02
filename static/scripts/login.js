window.onload = function() {
    const sentence = document.getElementById('flipping-sentence');
    const words = sentence.innerText.split(' ');

    // Clear the original sentence
    sentence.innerHTML = '';

    words.forEach((word, index) => {
        const wordSpan = document.createElement('span');
        wordSpan.innerText = word;
        wordSpan.classList.add('flip-word'); // Add flip effect class
        
        // Apply delay so words flip one after another
        wordSpan.style.animationDelay = `${index * 1.5}s`;

        sentence.appendChild(wordSpan);
        sentence.appendChild(document.createTextNode(" ")); // Add space between words
    });
};
