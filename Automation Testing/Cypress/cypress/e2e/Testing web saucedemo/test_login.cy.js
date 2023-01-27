describe('Login', () => {
    it('Successfull Login', () => {
        cy.visit('https://www.saucedemo.com')
        cy.get('[data-test="username"]').type('standard_user')
        cy.get('[data-test="password"]').type('secret_sauce')
        cy.get('[data-test="login-button"]').click()
        cy.url().should('include', 'https://www.saucedemo.com/inventory.html')

    })
    it('Failed Login Invalid Username', () => {
        cy.visit('https://www.saucedemo.com')
        cy.get('[data-test="username"]').type('yanto')
        cy.get('[data-test="password"]').type('yantobasna')
        cy.get('[data-test="login-button"]').click()

    })
})