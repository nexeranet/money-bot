function sep(str, delimeter){
    return str.replace(/\B(?=(\d{3})+(?!\d))/g ,`${delimeter}`)
}
