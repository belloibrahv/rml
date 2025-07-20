// Main JavaScript file for CAREER SYSTEM

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    // Handle smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add active class to current navigation item
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    // Mobile menu toggle (if needed)
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Add loading animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.feature-card, .dashboard-card, .summary-card');
    animateElements.forEach(el => {
        observer.observe(el);
    });

    // Form validation helpers
    window.validateForm = function(formElement) {
        const inputs = formElement.querySelectorAll('input[required]');
        let isValid = true;
        
        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.classList.add('error');
                isValid = false;
            } else {
                input.classList.remove('error');
            }
        });
        
        return isValid;
    };

    // Show/hide password functionality
    const passwordToggles = document.querySelectorAll('.password-toggle');
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            const type = input.type === 'password' ? 'text' : 'password';
            input.type = type;
            this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
        });
    });

    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });

    // Add tooltip functionality
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
        });
        
        element.addEventListener('mouseleave', function() {
            const tooltip = document.querySelector('.tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
});

// Utility functions
window.utils = {
    // Format date
    formatDate: function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    },

    // Format percentage
    formatPercentage: function(value) {
        return Math.round(value * 100) / 100 + '%';
    },

    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Show notification
    showNotification: function(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 3000);
    },

    // Copy to clipboard
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(() => {
            this.showNotification('Copied to clipboard!', 'success');
        }).catch(() => {
            this.showNotification('Failed to copy', 'error');
        });
    }
};

// API helper functions
window.api = {
    // Make API request
    request: async function(url, options = {}) {
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        
        const finalOptions = { ...defaultOptions, ...options };
        
        try {
            const response = await fetch(url, finalOptions);
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.message || 'API request failed');
            }
            
            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    // Get recommendations
    getRecommendations: function(skills, interests) {
        return this.request('/api/recommend', {
            method: 'POST',
            body: JSON.stringify({ skills, interests })
        });
    },

    // Get analytics
    getAnalytics: function() {
        return this.request('/api/analytics');
    },

    // Get careers
    getCareers: function() {
        return this.request('/api/careers');
    }
};

// Local Storage Management
window.localStorageManager = {
    // Store recommendation in local storage
    saveRecommendation: function(recommendation) {
        try {
            const recommendations = this.getRecommendations();
            recommendation.id = Date.now(); // Unique ID
            recommendation.timestamp = new Date().toISOString();
            recommendations.unshift(recommendation); // Add to beginning
            
            // Keep only last 50 recommendations
            if (recommendations.length > 50) {
                recommendations.splice(50);
            }
            
            localStorage.setItem('careerRecommendations', JSON.stringify(recommendations));
            return true;
        } catch (error) {
            console.error('Error saving recommendation:', error);
            return false;
        }
    },

    // Get all recommendations from local storage
    getRecommendations: function() {
        try {
            const stored = localStorage.getItem('careerRecommendations');
            return stored ? JSON.parse(stored) : [];
        } catch (error) {
            console.error('Error getting recommendations:', error);
            return [];
        }
    },

    // Get recommendation by ID
    getRecommendationById: function(id) {
        const recommendations = this.getRecommendations();
        return recommendations.find(rec => rec.id === id);
    },

    // Delete recommendation by ID
    deleteRecommendation: function(id) {
        try {
            const recommendations = this.getRecommendations();
            const filtered = recommendations.filter(rec => rec.id !== id);
            localStorage.setItem('careerRecommendations', JSON.stringify(filtered));
            return true;
        } catch (error) {
            console.error('Error deleting recommendation:', error);
            return false;
        }
    },

    // Clear all recommendations
    clearAllRecommendations: function() {
        try {
            localStorage.removeItem('careerRecommendations');
            return true;
        } catch (error) {
            console.error('Error clearing recommendations:', error);
            return false;
        }
    },

    // Get statistics
    getStats: function() {
        const recommendations = this.getRecommendations();
        return {
            total: recommendations.length,
            thisMonth: recommendations.filter(rec => {
                const recDate = new Date(rec.timestamp);
                const now = new Date();
                return recDate.getMonth() === now.getMonth() && 
                       recDate.getFullYear() === now.getFullYear();
            }).length,
            averageConfidence: recommendations.length > 0 ? 
                recommendations.reduce((sum, rec) => sum + (rec.confidence || 0), 0) / recommendations.length : 0
        };
    }
};

// Add CSS for animations and notifications
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 6px;
        color: white;
        font-weight: 500;
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    }
    
    .notification.show {
        transform: translateX(0);
    }
    
    .notification-success {
        background: #28a745;
    }
    
    .notification-error {
        background: #dc3545;
    }
    
    .notification-info {
        background: #17a2b8;
    }
    
    .tooltip {
        position: absolute;
        background: #333;
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 0.85rem;
        z-index: 1000;
        pointer-events: none;
    }
    
    .tooltip::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 5px solid transparent;
        border-top-color: #333;
    }
    
    .input.error {
        border-color: #dc3545;
    }
    
    .mobile-menu-toggle {
        display: none;
    }
    
    @media (max-width: 768px) {
        .mobile-menu-toggle {
            display: block;
        }
        
        .nav-menu {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            flex-direction: column;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transform: translateY(-100%);
            opacity: 0;
            transition: all 0.3s ease;
        }
        
        .nav-menu.active {
            transform: translateY(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);
