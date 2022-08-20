from mvc_flask import Router

Router.get('/', 'home#home')
Router.get('/updates', 'home#updates')
Router.get('/about', 'home#about')


Router.get('/login', 'login#login')
Router.post('/login', 'login#login')
Router.get('/login/logout', 'login#logout')
Router.get('/login/newaccount', 'login#new_account')
Router.post('/login/newaccount', 'login#new_account')
Router.get('/login/recover', 'login#recover_password')
Router.post('/login/recover', 'login#recover_password')
Router.get('/login/recover/validate-token', 'login#validate_token')
Router.post('/login/recover/validate-token', 'login#validate_token')


Router.get('/profile', 'profile#home')
Router.get('/arena', 'arena#home')
Router.get('/world', 'world#home')
Router.get('/marketplace', 'marketplace#home')
Router.get('/character', 'character#home')
Router.get('/tavern', 'tavern#home')
Router.get('/settings', 'settings#home')
