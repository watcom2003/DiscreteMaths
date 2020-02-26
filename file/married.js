function married(x , y) {
        var family = [ {"husband":"jack","wife":"jill"}, {"husband":"homer","wife":"marge"},{"husband":"bill","wife":"ben"} ]
        var marry = false;
       
        for (i=0; i< family.length; i++) {
              if ((x==family[i].husband) && (y==family[i].wife)) { marry = true}
        }
        return(marry)
}
