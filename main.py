def dmr(nummer, deler):
  stopswitch = 0
  deler = int(deler)
  nummer = int(nummer)
  ateller = 1
  ateller = int(ateller)
  rbereken = deler
  rbereken = int(rbereken)
  if nummer == 0:
    print("Kan niet door 0 delen")
    stopswitch = 1
  while rbereken <= nummer:
      if stopswitch == 0:
        if deler == 0:
          print("Kan niet door 0 delen")
          stopswitch = 1
          break
      else:
        break
      rbereken = rbereken + deler
      ateller = ateller + 1
  if rbereken > nummer:
      rbereken = rbereken - deler
      ateller = ateller - 1
      rest = nummer - rbereken
  if stopswitch == 1:
      ateller = 0
      rest = 0
      stopswitch = 0
  else:
    print ("Rest:", rest)
    print ("Antwoord:", ateller)