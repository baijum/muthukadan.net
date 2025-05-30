// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu functionality
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const mobileNavClose = document.querySelector('.mobile-nav-close');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileNavToggle && mobileNavClose && mainNav) {
        mobileNavToggle.addEventListener('click', function() {
            mainNav.classList.add('mobile-active');
            mobileNavClose.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
        });
        
        mobileNavClose.addEventListener('click', function() {
            mainNav.classList.remove('mobile-active');
            mobileNavClose.classList.remove('active');
            document.body.style.overflow = ''; // Re-enable scrolling
        });
        
        // Close mobile menu when a link is clicked
        mainNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                mainNav.classList.remove('mobile-active');
                mobileNavClose.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Only apply to actual hash links (starting with #), not regular navigation links
        if (anchor.getAttribute('href').startsWith('#')) {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                
                if (targetId === '#') return;
                
                e.preventDefault();
                
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            });
        }
    });
    
    // Add active class to current nav item based on URL
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.main-nav a');
    const currentPage = currentLocation.split('/').pop();
    
    navLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        
        if (linkHref === currentPage || 
            (currentPage === '' && (linkHref === '/' || linkHref === 'index.html')) ||
            (currentPage.includes('posts/') && linkHref === 'posts.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
    
    // Theme toggle functionality (can be implemented in the future)
    
    // Back to top button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<span class="material-icons">arrow_upward</span>';
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: var(--primary-color);
        color: white;
        border: none;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease, transform 0.3s ease;
        z-index: 1000;
        box-shadow: var(--elevation-2);
    `;
    document.body.appendChild(backToTopBtn);
    
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.style.opacity = '1';
            backToTopBtn.style.transform = 'translateY(0)';
        } else {
            backToTopBtn.style.opacity = '0';
            backToTopBtn.style.transform = 'translateY(20px)';
        }
    });
    
    // Image lazy loading
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
        document.body.appendChild(script);
    }
});

// Add estimated reading time to blog posts
function addReadingTime() {
    const postContent = document.querySelector('.post-content');
    if (!postContent) return;
    
    const text = postContent.textContent;
    const wordCount = text.split(/\s+/).length;
    const readingTime = Math.ceil(wordCount / 200); // Assuming 200 words per minute reading speed
    
    const readingTimeElement = document.createElement('span');
    readingTimeElement.className = 'reading-time';
    readingTimeElement.innerHTML = `<span class="material-icons">schedule</span> ${readingTime} min read`;
    
    const postMeta = document.querySelector('.post-meta');
    if (postMeta) {
        postMeta.appendChild(readingTimeElement);
    }
}

// Execute reading time function if on a blog post page
if (window.location.pathname.includes('/posts/')) {
    document.addEventListener('DOMContentLoaded', addReadingTime);
}

// Simple form validation for contact form
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        let isValid = true;
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const messageInput = document.getElementById('message');
        
        // Simple validation
        if (nameInput.value.trim() === '') {
            isValid = false;
            nameInput.style.borderColor = 'var(--error)';
        } else {
            nameInput.style.borderColor = '#e0e0e0';
        }
        
        if (emailInput.value.trim() === '' || !isValidEmail(emailInput.value)) {
            isValid = false;
            emailInput.style.borderColor = 'var(--error)';
        } else {
            emailInput.style.borderColor = '#e0e0e0';
        }
        
        if (messageInput.value.trim() === '') {
            isValid = false;
            messageInput.style.borderColor = 'var(--error)';
        } else {
            messageInput.style.borderColor = '#e0e0e0';
        }
        
        if (isValid) {
            // In a real implementation, you would send the form data to a server
            // For now, we'll just show an alert
            alert('Thank you for your message! I will get back to you soon.');
            this.reset();
        } else {
            alert('Please fill out all required fields correctly.');
        }
    });
}

// Email validation helper function
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
