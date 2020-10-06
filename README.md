# Error pages  

**This repository** includes pages for http errors. You can generate them by running python script `./src/builder.py`. Also in the folder ***builded*** you can find builded templates.

---

You can view [an example for 404](https://nvg-group.com/404)   
    
## Usage

**Use**. You can use builded templates in `./builded/*`

**Configure**. Type all error what you need in `./src/builder.py`

    ListErrors=(400,401,402,403,404,405,500,502,503,504,505,526)
    
**Template**. Use `./src/template.html` and `./res/error.css` for *hack* styled template or make up them yourself.  

**Javascript**. If you want, you can use [particles.js](https://github.com/VincentGarreau/particles.js/) for background. You can change .json config file in `./res/particlesjs-config.php` if you use ***PHP***. Otherwise rename the file to .json  

**Build**. Run Python script

## Build

    $ python3 ./src/builder.py
or
    
    $ python ./src/builder.py
    
## License  
Apache-2.0 License
