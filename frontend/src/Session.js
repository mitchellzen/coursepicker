var Session = (function () {
    var instance;
 
    function createInstance() {
        var object = new Object("Signed in user");
        return object;
    }
 
    return {
        getInstance: function () {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        }
    };
})();