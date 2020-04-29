# UpgradeMe

This programs allows you to generate a boarding pass barcode from an image.

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

