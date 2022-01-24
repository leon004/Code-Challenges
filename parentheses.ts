function isValid(s: string): boolean {
    const pila = [];     
    const hash = {
        "(": ")",
        "[": "]", 
        "{": "}"
    };


    for(let index = 0; index < s.length; index++){
        const simbolo = s[index];
        if(hash[simbolo]){
            pila.push(hash[simbolo]);
            continue;
        }

        const popped = pila.pop();

        if (popped !== simbolo){
            return false;
        }

    }
    return pila.length ===0;
}

