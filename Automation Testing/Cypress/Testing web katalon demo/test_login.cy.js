describe('Login', () => {
    it('Successfull Login', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type('John Doe')
        cy.get('#txt-password').type('ThisIsNotAPassword')
        cy.get('#btn-login').click()
        cy.url().should('include', 'https://katalon-demo-cura.herokuapp.com/#appointment')

    })
    it('Failed Login Invalid Username', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type('Yanto')
        cy.get('#txt-password').type('ThisIsNotAPassword')
        cy.get('#btn-login').click()
        cy.get('.text-danger')

    })

    it('Failed Login Invalid Password', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type('John Doe')
        cy.get('#txt-password').type('Yantonal123')
        cy.get('#btn-login').click()

    })
    it('Failed Login Invalid Username & Password', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type('Yanto')
        cy.get('#txt-password').type('Yantonal123')
        cy.get('#btn-login').click()
        cy.get('.text-danger')

    })

    it('Failed Login Blank Field', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type(' ')
        cy.get('#txt-password').type(' ')
        cy.get('#btn-login').click()
        cy.get('.text-danger')

    })
})
