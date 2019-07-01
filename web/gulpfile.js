const { series, src, dest} = require('gulp');

var concat = require('gulp-concat');
var uglify = require('gulp-terser');
var renmae = require('gulp-rename');

function compile_js() {
  return src([
    'node_modules/jquery/dist/jquery.slim.min.js',
    'node_modules/popper.js/dist/popper.min.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js'
  ])
    .pipe(concat('all.min.js'))
    .pipe(uglify())
    .pipe(dest('static/js'))
}

function compile_css() {
  return src([
    'node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concat('all.min.css'))
    .pipe(dest('static/css'))
}

exports.default = series(compile_js, compile_css);
