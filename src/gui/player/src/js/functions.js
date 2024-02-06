function videoPlayerStart() {
    var videoElement = $('.video-block video').get(0);

    if (videoElement) {
        videoElement.play().catch(function (error) {
            //console.error("Error attempting to play video:", error);
        });
    }
}

function videoPlayerStop() {
    var videoElement = $('.video-block video').get(0);

    if (videoElement) {
        if (!videoElement.paused) {
            videoElement.pause();
        }

        videoElement.currentTime = 0;
    }
}

export function updateData({ type, src, text, textColor, borderColor, backgroundColor }) {
    switch (type) {
        case 'black':
            $('.block').hide();
            $('.black-block').show();
            break;
        case 'image':
            videoPlayerStop();

            $('.black-block').hide();
            $('.video-block').hide();

            $('.text-block').css('background-color', 'transparent');

            $('.image-block').css('background-image', `url(${src})`).show();
            break;
        case 'video':
            $('.black-block').hide();
            $('.image-block').hide();

            $('.text-block').css('background-color', 'transparent');

            $('.video-block video').attr('src', src).parent().show();

            videoPlayerStart();

            break;
        case 'text':
            const textBlock = $('.text-block').text(text);

            if (textColor) {
                textBlock.css('color', textColor);
            }

            if (borderColor) {
                textBlock.css('text-shadow', `-1px -1px 0 ${borderColor}, 1px -1px 0 ${borderColor}, -1px 1px 0 ${borderColor}, 1px 1px 0 ${borderColor}`);
            }

            if (backgroundColor) {
                textBlock.css('background-color', backgroundColor);

                $('.video-block').hide();
                $('.image-block').hide();

                videoPlayerStop();
            } else {
                textBlock.css('background-color', 'transparent');
            }

            textBlock.show();

            break;
    }
}
