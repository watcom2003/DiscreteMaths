function married(x , y) {
        var family = "[ {'husband':'jack','wife':'jill'}, {'husband':'homer','wife':'marge'},{'husband':'bill','wife':'ben'} ]"
        var marry = false;
        var fam = JSON.parse(family)
        for (i=0; i< 3; i++) {
              if ((x==fam[i].husband) && (y==fam[i].wife)) { marry = true}
        }
        return(marry)
}
