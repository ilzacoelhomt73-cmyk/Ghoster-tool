const readline = require("readline");
const Kahoot = require("kahoot.js-latest");
const { fakerPT_BR: faker } = require("@faker-js/faker");

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const RESET = '\x1b[0m';

const PRETO       = '\x1b[30m';
const VERMELHO    = '\x1b[31m';
const VERDE       = '\x1b[32m';
const AMARELO     = '\x1b[33m';
const AZUL        = '\x1b[34m';
const MAGENTA     = '\x1b[35m';
const CIANO       = '\x1b[36m';
const BRANCO      = '\x1b[37m';

const PRETO_B     = '\x1b[90m';
const VERMELHO_B  = '\x1b[91m';
const VERDE_B     = '\x1b[92m';
const AMARELO_B   = '\x1b[93m';
const AZUL_B      = '\x1b[94m';
const MAGENTA_B   = '\x1b[95m';
const CIANO_B     = '\x1b[96m';
const BRANCO_B    = '\x1b[97m';

const client = new Kahoot();

console.log(`${VERMELHO_B}
██████╗  ██████╗ ████████╗███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██████╔╝██║   ██║   ██║   ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██║   ██║   ██║   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝   ██║   ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

${RESET}${BRANCO_B}[ + ] CRIADO POR ARTHUR [ + ]
${RESET}
`);

r1.question("PIN => ", (pin) => {
    const pin_partida = Number(pin);

    r1.question("NOMES ALEATORIOS? [y/n]: ", (nomes_aleatorios) => {

        if (nomes_aleatorios.toLowerCase() == "y") {

            r1.question("QUANTIDADE DE BOTS => ", (quantidade) => {
                r1.close();
                
                for (let i = 0; i < Number(quantidade); i++) {
                    const Bot = new Kahoot(); 
                    const BotName = faker.internet.username() + i;
                    
                    Bot.on("Joined", () => {
                        console.log(`${VERDE}[ + ] ${BotName} entrou na partida${RESET}`);
                    });

                    setTimeout(() => {
                        Bot.join(pin_partida, BotName).catch(() => {});
                    }, i * 300);
                }
            });
        } else {
            r1.question("QUANTIDADE DE BOTS => ", (quantidade) => {
                r1.question("NOME => ", (nome_escolhido) => {
                    r1.close();
                    
                    for (let i = 0; i < Number(quantidade); i++) {
                        const Bot = new Kahoot(); 
                        const BotName = `${nome_escolhido}${i + 1}`;
                        
                        Bot.on("Joined", () => {
                            console.log(`${VERDE}[ + ] ${BotName} entrou na partida${RESET}`);
                        });

                        setTimeout(() => {
                            Bot.join(pin_partida, BotName).catch(() => {});
                        }, i * 300);
                    }
                });
            });
        }

    });
});

