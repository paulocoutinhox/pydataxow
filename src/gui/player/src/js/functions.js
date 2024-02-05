export function updateData({ type, src, text, textColor, borderColor, backgroundColor }) {
    switch (type) {
        case 'black':
            $('.block').hide();
            $('.black-block').show();
            break;
        case 'image':
            $('.black-block').hide();
            $('.video-block').hide();

            $('.video-block video').get(0).pause();
            $('.video-block video').get(0).currentTime = 0;

            $('.text-block').css('background-color', 'transparent');

            $('.image-block').css('background-image', `url(${src})`).show();
            break;
        case 'video':
            $('.black-block').hide();
            $('.image-block').hide();

            $('.text-block').css('background-color', 'transparent');

            $('.video-block video').attr('src', src).parent().show();
            $('.video-block video').get(0).play();
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

                $('.video-block video').get(0).pause();
                $('.video-block video').get(0).currentTime = 0;
            } else {
                textBlock.css('background-color', 'transparent');
            }

            textBlock.show();

            break;
    }
}
