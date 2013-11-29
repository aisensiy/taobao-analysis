pwd=`pwd`
current_dir=`basename $pwd`
echo $current_dir
target=212
echo $current_dir
rsync -r `pwd` $target:
ssh 212 "sed -i 's/localhost/162.105.11.33/g' ~/$current_dir/frontend/app/scripts/app.js"
# ssh 212 'god restart taobao-backend'
# ssh 212 'god restart taobao-frontend'
