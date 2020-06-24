# UpgradeMe

This programs allows you to generate a boarding pass barcode from an image. 

> DISCLAIMER : Only for educational or some research purpose of course

## How it works 

1. Take a picture of your boarding pass, make sure the bar code is visible
2. Run the program using the picture you just took
3. The program will decode the bar code, get the company and update :
  - Your seat
  - You class (ex: from standard to premium)
4. A new bar code is generated with the upgraded informations

## How to use it

``` bash
./upgradeMe </path/to/image>
```

## Flying company supported 

- Luftansa

## Todo 

- Secure the code
- Add more companies
- Allow users to just change their information such as seat number, name etc. 
- Create an API, to do it remotly by just sending a picture of the boarding pass and getting the updated one directly

## UPDATE et j'ai la flemme de tout changer le readme pour le moment : 

Pour build le container : 
```bash
docker build -t victor-fly .
# puis
docker run -d victor-fly
```

Ensuite il faut aller sur `127.0.0.1` ou votre IP, puis que vous selectionnez un fichier avec un code bar. Le serveur genere une nouvelle image et vous la renvoie. 