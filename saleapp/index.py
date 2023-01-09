from flask import render_template, request, redirect, url_for
from saleapp import app, login
import utils
import math
import cloudinary.uploader
from flask_login import login_user, logout_user

@app.route("/")
def home():

    # cates = utils.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    page = request.args.get('page', 1)
    products = utils.load_products(cate_id=cate_id, kw=kw, page=int(page))
    counter = utils.count_products()

    # return render_template('index.html',
    #                        categories=cates,
    #                        products=products,
    #                        pages=math.ceil(counter/app.config['PAGE_SIZE']))
    return render_template('index.html',
                           products=products,
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))

# @app.route("/products")
# def product_list():
#     products = utils.load_products()
#
#     return render_template('products.html',
#                            products=products)

@app.route('/register', methods=['get', 'post'])
def user_register():
    err_msg=""

    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        avatar_path = None

        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url']

                utils.add_user(name=name, username=username, password=password, email=email, avatar=avatar_path)
                # return redirect(url_for('home'))
                return redirect(url_for('user_signin'))
            else:
                err_msg = 'Mat khau KHONG khop!!!'
        except Exception as ex:
            err_msg = 'He thong co loi!!!' + str(ex)
        # else:
        #     return redirect(url_for('home'))

    # cates = utils.load_categories()

    # return render_template('register.html', err_msg=err_msg, categories=cates)
    return render_template('register.html', err_msg=err_msg)

@app.route('/user-login', methods=['get', 'post'])
def user_signin():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            err_msg = 'Username hoac password khong chinh xac!!!'

    return render_template('login.html', err_msg=err_msg)

@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))


@app.context_processor # doan nay de goi categories trong moi function tranh lap lai
def common_respone():
    return {
        'categories': utils.load_categories()
    }

@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    products = utils.load_products(cate_id=cate_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template('products.html',
                           products=products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)

    return render_template('product_detail.html',
                           product=product)

if __name__ == '__main__':
    from saleapp.admin import *
    app.run(debug=True)

