import math

from colorama import Fore

print(Fore.RED+"""
                        
                         ....----....                    
                    ..-:"''         ''"-..
                 .-'                      '-.
               .'              .     .       '.
             .'   .          .    .      .    .''.
           .'  .    .       .   .   .     .   . ..:.
         .' .   . .  .       .   .   ..  .   . ....::.
        ..   .   .      .  .    .     .  ..  . ....:IA.
       .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
      .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
      '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
     .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
    .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
    ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
   .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
  .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
  :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
  ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
  ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
  :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
  '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
   :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
  .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
  ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
: .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
:.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
  "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
   :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
   :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
   :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
   :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
   :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
   ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
     V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
       'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
        I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
       .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
       :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
       :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
       ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
       ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
       :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
       ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
         "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
          ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
            "::....::.:::..:..::IIIIIHHHHMMMHHMV"
              "::.::.. .. .  ...:::IIHHMMMMHMV"
                "V::... . .I::IHHMMV"'
                  '"VHVHHHAHHHHMMV:"'

    
                                                                

""")



print("DECODER RSA")
# Definindo as variáveis
c = int(input('x: '))
n = int(input('x: '))
e = int(input('x: '))
p = int(input('x: '))
q = int(input('x: '))

# Calculando phi
phi = (p - 1) * (q - 1)

# Calculando d (inverso modular)
def modInverse(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    return x1 if x1 >= 0 else x1 + m0

d = modInverse(e, phi)

# Calculando m (mensagem decodificada)
def modPow(base, exponent, modulus):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus

    return result

m = modPow(c, d, n)

# Função para converter BigInt para bytes
def BigIntToBytes(bigIntValue):
    hexString = hex(bigIntValue)[2:]
    paddedHexString = '0' * (len(hexString) % 2) + hexString
    return bytes.fromhex(paddedHexString)

resultBytes = BigIntToBytes(m)
print(resultBytes.hex())

# Função para decodificar hexadecimal para texto
def hexToText(hexString):
    hexString = hexString.replace(' ', '').lower()

    if not all(c in '0123456789abcdef' for c in hexString):
        raise ValueError('String hexadecimal inválida')

    return bytes.fromhex(hexString).decode('utf-8')

decodedText = hexToText(resultBytes.hex())
print('Texto decodificado:', decodedText)