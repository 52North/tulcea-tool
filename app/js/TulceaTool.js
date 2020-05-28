requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'TulceaTool': '../TulceaTool',
        'data': '../data/'
    }
});

requirejs(['TulceaTool/main']);
