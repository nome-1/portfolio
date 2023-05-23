const express=require("express");
const morgan=require("morgan");
const app=express();
const logger=require("./logger")
const courses = require('./routes/courses');

app.use(express.json());
app.use(logger)
app.use(express.static('public')); //to use object stored in public use {/objectName}
app.use('/api/courses',courses)

if (app.get('env') === 'development') {
    app.use(morgan('tiny'));
    console.log('Morgan enabled...');
}

app.set('view engine', 'pug');
app.set('views', './views'); // default

app.get('/',(req, res)=>{
    res.render('index',{title:"my app",message:'hello world'})
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`));